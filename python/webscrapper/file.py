def save_to_file(file_name, jobs):
    # write results to file
    file = open(f"{file_name}.csv", "w", encoding='utf-8')

    for job in jobs:
        data = f"{job['position']},{job['company']}, {job['location']}, {job['link']}\n"
        file.write(data)

    file.close()
