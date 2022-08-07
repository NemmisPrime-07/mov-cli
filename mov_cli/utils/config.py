import platform
import os
class config:
    def __init__(self):
        pass

    @staticmethod
    def winorlinux():
        plt = platform.system()
        if plt == "Windows":
            return f"C://Users//{os.getenv('username')}//Documents"
        elif (plt == "Linux") or (plt == "Darwin"):
            return f"/home/{os.getlogin()}/Documents"
    
    @staticmethod
    def setprovider(provider):
        if os.path.exists(f"{config.winorlinux()}//mov_cli"):
            pass
        else:
            os.mkdir(f"{config.winorlinux()}//mov_cli")
        file = f"{config.winorlinux()}//mov_cli//.provider"
        with open(file, "a") as f:
            f.truncate(0)
            f.write(f"provider: {provider}")
    
    @staticmethod
    def getprovider():
        if config.providerexists() is True:
            file = f"{config.winorlinux()}//mov_cli//.provider"
            with open(file, "r") as f:
                # get what stands after "provider: "
                provider = f.read().split("provider: ")[1]
                if provider == "actvid" or "theflix" or "sflix" or "solar":
                    return provider
                else:
                    return "theflix"
        else:
            return "theflix"
        
    @staticmethod
    def providerexists():
        file = f"{config.winorlinux()}//mov_cli//.provider"
        if os.path.exists(file):
            return True
        else:
            return False

