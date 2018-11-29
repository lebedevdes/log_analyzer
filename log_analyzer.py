






if __name__ == '__main__':
    log_path = "logs/tochkac.log"
    date = "22.11.2018"
    time_h = "22"
    res = ""
    message = "Send "
    with open(log_path) as log:
        for line in log:
            if line.find("{} {}".format(date, time_h)) >= 0:
                if line.find(message) >= 0:
                    res += line

    print(res)