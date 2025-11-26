# Match is same as the Switch Case

def httpsStatus(status):
    match status:
        case 200:
            return "Ok All Good"
        case 404:
            return "Not Fount Error"
        case 401:
            return "Forbideen Error"
        case _:
            return "Unknown Error"
        
print(httpsStatus(200))