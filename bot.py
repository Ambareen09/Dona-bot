import re
import pandas as pd

course_df = pd.read_csv('courses.csv', index_col="ID")
print(course_df)
degree_lvl = None
stream = None
code = None
while True:
    ip = input()
    if ip == "kill":
        break
    print(ip)
    x = re.search(r'register', ip)
    if x:
        if not degree_lvl:
            print("Okay, tell me your degree level")
            resp = input()
            # print(re.findall(r"((master\'?s?)|(bachelor\'?s?)|(doctor?(ate)?))", resp, flags=re.IGNORECASE))
            degree_lvl_match = re.search(
                r"((master\'?s?)|(bachelor\'?s?)|(doctor?(ate)?))", resp, flags=re.IGNORECASE)
            print(degree_lvl_match.groups())
            degree_lvl = degree_lvl_match.group(0)
        if not stream:
            print(
                f"Okay, in which stream are you pursuing your {degree_lvl.capitalize()} degree?")
            resp = input()
            stream_match = re.search(
                r"((computer science)|(physics))", resp, flags=re.IGNORECASE)
            print(stream_match.groups())
            stream = stream_match.group(0)
            code = ''.join([c.capitalize() for c in stream.split()])

        print(
            f"Okay, Here are the courses available for {degree_lvl} degree {stream} program:")
        print(course_df[course_df.index.str.startswith("CS")]
              ["name"].to_string())

    else:
        print("Sorry, could you please rephrase.")
        print(x)
        break
