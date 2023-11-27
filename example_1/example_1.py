from snowflake import *

user_input = "."

# Create a new Snowflake object
snowflake = Snowflake()

# Create a new EchoProc object
proc = AddDotProc()

# Set the proc of the Snowflake object to the EchoProc object
result = snowflake.proc(proc) \
    .chain("example_1/prompt.md") \
    .chain("example_1/prompt.md") \
    .chain("example_1/prompt.md") \
    .prompt(user_input)

# Print the result
print(result._proc_history)