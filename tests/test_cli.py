import subprocess

def get_location_details(query):
    commands = ["bin\\geoloc-util.bat"]
    commands.extend(query)
    result = subprocess.run(commands, capture_output=True)
    result_lines = str(result.stdout).split("\\n")
    output_lines = result_lines[6 : len(result_lines) - 1]
    return ' '.join(output_lines)

def test_with_single_name():
    actual_result = get_location_details(["--locations", "\"Madison, WI\""])
    expected_result = "[ { name: \\'Madison\\', lat: 43.074761, long: -89.3837613 } ]"
    assert actual_result == expected_result

def test_with_single_zip_code():
    actual_result = get_location_details(["--locations", "12345"])
    expected_result = "[ { name: 'Schenectady', lat: 42.8142, long: -73.9396 } ]"
    assert actual_result == expected_result

def test_with_locations_flag():
    actual_result = get_location_details(["--locations", "\"Madison, WI\"", "12345"])
    expected_result = "[   { name: \\'Madison\\', lat: 43.074761, long: -89.3837613 },   { name: \\'Schenectady\\', lat: 42.8142, long: -73.9396 } ]"
    assert actual_result == expected_result

def test_with_mutliple_names_and_zips():
    actual_result = get_location_details(["\"Madison, WI\"", "12345", "Chicago, IL", "10001"])
    expected_result = "[   { name: \\'Madison\\', lat: 43.074761, long: -89.3837613 },   { name: \\'Schenectady\\', lat: 42.8142, long: -73.9396 },   { name: \\'Chicago\\', lat: 41.8755616, long: -87.6244212 },   { name: \\'New York\\', lat: 40.7484, long: -73.9967 } ]"
    assert actual_result == expected_result

def test_with_unknown_location():
    actual_result = get_location_details(["bla"])
    expected_result = "[ {} ]"
    assert actual_result == expected_result
