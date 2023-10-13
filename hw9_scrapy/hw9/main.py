import asyncio
from spiders.main_spider import run_spiders
from mongodb_module.download_jsons import main_download_json

async def main():
    await run_spiders()
    
    print("GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOD")
    
    main_download_json()
    
    
if __name__ == "__main__":
    asyncio.run(main())
