def is_report_safe(report):
    type = ''
    i = 0
    while i < len(report)-1:
        prev_type = type
        diff = report[i+1] - report[i]

        if 1 <= diff <= 3:
            type = 'increasing'

            if prev_type == type or prev_type == '':
                i += 1
                continue
            else:
                return False
        elif -3 <= diff <= -1:
            type = 'decreasing'

            if prev_type == type or prev_type == '':
                i += 1
                continue
            else:
                return False
        else:
            # If neither increasing or decreasing, report is not safe
            return False
        
        i += 1

    return True

def main():
    contents = None
    with open('input.txt') as file:
        contents = file.readlines()

    contents = [line.split() for line in contents]

    for i, line in enumerate(contents):
        contents[i] = [int(num) for num in line]

    safe_reports = []
    for report in contents:
        safe_reports.append(is_report_safe(report))

    num_safe_reports = 0
    for report in safe_reports:
        if report == True:
            num_safe_reports += 1

    print(num_safe_reports)

if __name__ == '__main__':
    main()