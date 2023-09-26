import argparse
import json
from pathlib import Path


parser = argparse.ArgumentParser(
    description="A tool to help analyse the properties of objects in The Legend of Zelda: Skyward Sword (HD)."
)

parser.add_argument(
    "--stages",
    nargs="*",
    help="A list of stages to include in the search. If none are given, all stages will be included.",
)
parser.add_argument(
    "--names",
    nargs="*",
    help="A list of object names to include in the search. If none are given, all names will be included.",
)
parser.add_argument(
    "--types",
    nargs="*",
    help="A list of the object types to include in the search. If none are given, all types will be included.",
)
parser.add_argument(
    "--attribute",
    nargs="?",
    help="Only include objects with the given attribute. This attribute is the subject of any shifts or masks also defined. If no attribute is given, param1 is used.",
)
parser.add_argument(
    "--shift",
    nargs="?",
    help="The number of bits to shift the attribute by. If no attribute is given, param1 is used.",
)
parser.add_argument(
    "--mask",
    nargs="?",
    help="The mask applied to the attribute. If no attribute is given, param1 is used.",
)
parser.add_argument(
    "--hex",
    dest="as_hex",
    action="store_true",
    help="Determines if integer values should be outputted in hexadecimal.",
)
parser.add_argument(
    "--bin",
    dest="as_bin",
    action="store_true",
    help="Determines if integer values should be outputted in binary.",
)
parser.add_argument(
    "--summary",
    action="store_true",
    help="If this argument is given, print a summary of all the unique results found.",
)

# parser.print_help()
args = parser.parse_args()


ROOT_STAGE_PATH = Path("./stageHD")
STAGE_PATHS = tuple(ROOT_STAGE_PATH.glob("*.json"))


def convert_value_to_str(value: int) -> str:
    if args.as_hex:
        return hex(value)
    elif args.as_bin:
        return bin(value)
    else:
        return str(value)


def print_object_and_result(
    object: dict,
    result: int,
    stage_name: str,
    layer_name: str,
    room_name: str,
    attribute: str,
):
    original_value = object[attribute]

    if type(original_value) is str:
        original_value = int("0x" + original_value.replace(" ", ""), 16)

    result = convert_value_to_str(result)

    if type(original_value) is int:
        original_value = convert_value_to_str(original_value)

    print(
        f"{object['name']:<10}\t{stage_name:<7} {layer_name:<3} {room_name:<3} {object['id']:<5} {attribute}: {original_value:<11} -> {result}"
    )
    # print(object)


def use_object(object, names: list[str], attribute) -> bool:
    if type(object) is not dict:
        return False

    if names and object.get("name") not in names:
        return False

    if attribute not in object:
        return False

    return True


def register_unique_result(result: int):
    if result in unique_results:
        unique_results[result] += 1
    else:
        unique_results[result] = 1


def analyse_object(
    object: dict, attribute: str, shift: str | int, mask: str | int
) -> int | None:
    if (value := object.get(attribute)) is None:
        return None

    if type(value) is str:
        value = int("0x" + value.replace(" ", ""), 16)

    # Convert shift string to int
    if type(shift) is str:
        if shift[0:2] == "0x":
            shift = int(shift[2:], 16)
        elif shift[0:2] == "0b":
            shift = int(shift[2:], 2)
        else:
            shift = int(shift)

    # Convert mask string to int
    if type(mask) is str:
        if mask[0:2] == "0x":
            mask = int(mask[2:], 16)
        elif mask[0:2] == "0b":
            mask = int(mask[2:], 2)
        else:
            mask = int(mask)

    if shift and shift > -1:
        value = value >> shift

    if mask and mask > -1:
        value = value & mask
    
    register_unique_result(value)

    return value


def analyse_objects(
    stage_path: Path,
    names: list[str] = [],
    types: list[str] = [],
    attribute: str = None,
    shift: int = -1,
    mask: int = -1,
):
    with stage_path.open("r") as f:
        stage_data = json.load(f)

    if not attribute:
        attribute = "params1"

    room_name = "-1"
    stage_name = stage_path.name.split(".json")[0]

    # Handle LAY
    layers = stage_data["LAY "]

    for layer_name in layers:
        layer = layers[layer_name]

        for object_group_name in layer:
            if types and object_group_name not in types:
                continue

            object_group = layer[object_group_name]

            for object in object_group:
                if not use_object(object, names, attribute):
                    continue

                result = analyse_object(object, attribute, shift, mask)

                print_object_and_result(
                    object, result, stage_name, layer_name, room_name, attribute
                )

    # Handle rooms
    rooms = stage_data["rooms"]

    for room_name in rooms:
        room = rooms[room_name]

        for object_group_name in room:
            if types and object_group_name not in types:
                continue

            if object_group_name == "LAY ":
                layers = room[object_group_name]

                for layer_name in layers:
                    layer = layers[layer_name]

                    for sub_object_group_name in layer:
                        if types and sub_object_group_name not in types:
                            continue

                        object_group = layer[sub_object_group_name]

                        for object in object_group:
                            if not use_object(object, names, attribute):
                                continue

                            result = analyse_object(object, attribute, shift, mask)

                            print_object_and_result(
                                object,
                                result,
                                stage_name,
                                layer_name,
                                room_name,
                                attribute,
                            )
            else:
                object_group = room[object_group_name]

                layer_name = "-1"

                for object in object_group:
                    if not use_object(object, names, attribute):
                        continue

                    result = analyse_object(object, attribute, shift, mask)

                    print_object_and_result(
                        object, result, stage_name, layer_name, room_name, attribute
                    )


unique_results = {}

for path in STAGE_PATHS:
    if args.stages and path.name.split(".json")[0] not in args.stages:
        continue

    analyse_objects(
        path,
        names=args.names,
        types=args.types,
        attribute=args.attribute,
        shift=args.shift,
        mask=args.mask,
    )

if args.summary:
    print("Unique Results:")

    for result in unique_results:
        result_str = convert_value_to_str(result)
        print(f"{result_str} occured {unique_results[result]} times")
