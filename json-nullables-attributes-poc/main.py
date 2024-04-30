#!/usr/bin/python

success = {
    "status": "success",
    "datas": [{
        "id": "1b4f49b0cdad4fc5bdec2f44f52dba67",
        "name": "John Doe"
    }]
}

error_1 = {
    "status": "fail",
    "datas": [{
        "id": "fba542d0d926405eaf2a1fc11b055805",
        "error": {
            "code": "CODE-1",
            "message": "Invalid request"
        }
    }]
    
}

error_2 = {
    "status": "fail",
    "datas": [{
        "id": "fba542d0d926405eaf2a1fc11b055805",
        "error": {
            "code": "CODE-2",
            "subCode": "SUB-CODE-2",
            "message": "Invalid scenario"
        }
    }]
}

error_3 = {
    "status": "fail",
    "datas": [{
        "id": "fba542d0d926405eaf2a1fc11b055805",
        "error": {
            "code": "CODE-3",
            "subCode": "SUB-CODE-3",
            "message": "Invalid new scenario"
        }
    }]
}


def handle_error_case_2(response):
    if response["status"] == "fail":
        for data in response["datas"]:
            if 'error' in data and 'subCode' in data.get('error') and "SUB-CODE-2" == data.get("error").get("subCode"):
                print("subCode 2 is present")
                return True
            else:
                print("subCode 2 is not present")
                return False

    print("Response is not an error")
    return False


def main():
    handle_error_case_2(success)
    handle_error_case_2(error_1)
    handle_error_case_2(error_2)
    handle_error_case_2(error_3)


if __name__ == '__main__':
    main()
