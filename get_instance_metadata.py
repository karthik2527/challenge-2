import requests
import json
import available_options
import sys

instance_metadata_url = "http://169.254.169.254/latest/meta-data/"
list_of_options = available_options.metadata_options


def get_all_metadata():
    """
    Get applicable metadata output
    :return: All the applicable metadata output for the instance as python dictionary
    """
    all_metadata_output = {}
    for option in list_of_options:
        resp = requests.get(instance_metadata_url + option)
        if resp.status_code == 200:
            all_metadata_output[option] = resp.text
    return all_metadata_output


def json_converter(result):
    """
    Converts the given python dictionary into json
    :param result: is a python dictionary
    :return: is an equivalent json
    """
    return json.dumps(result, indent=4)


def main():
    instance_metadata = get_all_metadata()
    if len(sys.argv) == 1:
        print(json_converter(instance_metadata))
        print(f"\nAWS provides {len(list_of_options)} metadata options not all options are applicable to all the EC2 "
              f"instances you can pass one of the keys above as argument to this script to retrieve specific metadata")
    elif len(sys.argv) == 2:
        required_metadata_output = {}
        required_key = sys.argv[1]
        required_value = instance_metadata[required_key]
        required_metadata_output[required_key] = required_value
        print(json_converter(required_metadata_output))
    else:
        print("Invalid input provided")


if __name__ == "__main__":
    main()
