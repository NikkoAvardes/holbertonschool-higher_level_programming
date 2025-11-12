#!/usr/bin/python3
""" Module for generating invitation letters
    from a template and a list of attendees.
"""


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template is not a string")
        return
    if not isinstance(attendees, list):
        print("Error: attendees is not a list")
        return
    if not all(isinstance(x, dict) for x in attendees):
        print("Error: attendees list does not contain only dicts")
        return
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))
        filename = f"output_{index}.txt"
        try:
            with open(filename, "w") as file:
                file.write(content)
        except Exception as e:
            print(f"Unexpected error writing {filename}: {e}")
