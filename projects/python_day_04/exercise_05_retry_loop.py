retry_count = 0
max_retries = 3
communication_successful = False

while retry_count < max_retries and communication_successful == False:
    print(f"Trying diagnostic request... attempt {retry_count + 1}")
    retry_count = retry_count + 1

if communication_successful == False:
    print(f"Diagnostic request failed after {max_retries} attempts.")