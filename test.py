import json
import re
from pprint import pprint

LINE_PATTERN = r"^(\w+)(((\[)|(\{)|(\(\()|(\())(\w+)((?(4)\])(?(5)\})(?(6)\)\))(?(7)\)(?!\)))))?-" \
               r"-((\w+)--)?>(\|(\w+)\|)?(\w+)(?#comment-" \
               r"-comment)(((\[)|(\{)|(\(\()|(\())(\w+)((?(17)\])(?(18)\})(?(19)\)\))(?(20)\)(?!\)))))?$"
LINE_REGEX_OBJECT = re.compile(LINE_PATTERN)

ELEMENT_TYPE_MAPPING = {
    "]": "rectangle",
    "}": "diamond",
    ")": "rounded_rectangle",
    "))": "circle"
}


def analysis(line):
    regex_match_object = LINE_REGEX_OBJECT.match(line)
    if not regex_match_object:
        print("illegal line")
        return False

    result_groups = regex_match_object.groups()
    print(result_groups)

    step_element = {
        "step_id": result_groups[0],
        "step_alias": result_groups[7],
        "step_type": ELEMENT_TYPE_MAPPING[result_groups[8]],
        "next": {
            "next_id": result_groups[13],
            "road_name": result_groups[10] or result_groups[12],
            "backup": {
                "backup_next_alias": result_groups[20],
                "backup_next_type": ELEMENT_TYPE_MAPPING[result_groups[21]]
            }
        }
    }
    return step_element


if __name__ == '__main__':
    e = analysis("input_10001((i1))--No-->|Yes|output_200001((o1))")
    print(json.dumps(e))
