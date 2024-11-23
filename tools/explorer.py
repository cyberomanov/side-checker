import json

import requests
from loguru import logger

from datatypes.airdrop import SideAirdropResponse
from tools.change_ip import execute_change_ip
from user_data.config import change_ip_url


def get_side_airdrop(index: int, address: str, session: requests.Session()) -> SideAirdropResponse:
    change_ip = execute_change_ip(change_ip_url=change_ip_url)
    if change_ip:
        logger.info(f"{index} | {address} | ip has been changed.")

    url = f"https://insider.side.one/airdrop/login/checkEligibility?address={address}"
    response = session.get(url=url)
    return SideAirdropResponse.parse_obj(json.loads(response.content))
