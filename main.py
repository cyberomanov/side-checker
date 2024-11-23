from loguru import logger

from tools.add_logger import add_logger
from tools.explorer import get_side_airdrop
from tools.other_utils import read_file, get_proxied_session
from user_data.config import mobile_proxy

if __name__ == '__main__':
    add_logger(version='v1.0')
    try:
        addresses = read_file(path='user_data/address.txt')
        session = get_proxied_session(proxy=mobile_proxy)
        total = 0
        for index, address in enumerate(addresses, start=1):
            try:
                airdrop = get_side_airdrop(index=index, address=address, session=session)
                if airdrop.totalAmount:
                    total += airdrop.totalAmount
                    criteria = sub_type_names = ", ".join([item.subTypeName for item in airdrop.items])
                    logger.success(f"{index} | {address}: {airdrop.totalAmount} $SIDE for [{criteria}].")
                else:
                    logger.info(f"{index} | {address}: not eligible.")
            except Exception as e:
                logger.exception(e)
        logger.info(f"total: {total} $SIDE.")
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        logger.exception(e)
