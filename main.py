import asyncio
import json
import logging
import logging.config
from dataclasses import dataclass

import yaml
from web3 import Web3
from web3._utils.filters import LogFilter


@dataclass
class FilterWrapper:
    event_filter: LogFilter
    pair_name: str
    oracle_address: str
    logger: logging.Logger


class BlockchainMonitor:

    def __init__(self):
        with open("spec.yaml", "r") as s:
            spec = yaml.safe_load(s)

        with open("logging.yaml", "r") as s:
            logging.config.dictConfig(yaml.safe_load(s))

        with open('abi.json', "r") as s:
            abi = json.load(s)

        w3 = Web3(Web3.HTTPProvider(spec['connection_settings']['alchemy_url']))

        # logger = logging.getLogger("test")
        # logger.info("Price changes in pair {}. Oracle address: {}. Current price: {}, block number: {}"
        #             .format(1,
        #                     2,
        #                     3,
        #                     4))

        self.filters = []
        pair_name_to_logger = {}

        for currency_pair in spec['currency_pairs']:
            for pair_name, pair_spec in currency_pair.items():
                for oracle_address in pair_spec['oracles_addresses']:
                    contract = w3.eth.contract(address=oracle_address, abi=abi)
                    pair_name_to_logger[pair_name] = pair_name_to_logger \
                        .get(pair_name, logging.getLogger(pair_name))
                    self.filters.append(FilterWrapper(
                        contract.events.AnswerUpdated.createFilter(fromBlock='latest'),
                        pair_name,
                        oracle_address,
                        pair_name_to_logger[pair_name]
                    ))

    @staticmethod
    def __handle_event(event, filter_wrapper):
        print("mehh")
        print("event args", event.args)
        print("current", event.args.current)
        print("block", event.args.blockNumber)
        # filter_wrapper.logger.info("test log")
        # filter_wrapper.logger.info("Price changes in pair {}. Oracle address: {}. Current price: {}, block number: {}"
        #                            .format(filter_wrapper.pair_name,
        #                                    filter_wrapper.oracle_address,
        #                                    event.args.current,
        #                                    event.args.blockNumber))

    async def __monitor(self, filter_wrapper, poll_interval):
        filter_wrapper.logger.info("Start monitor pair {}. Oracle address: {}".format(
            filter_wrapper.pair_name, filter_wrapper.oracle_address))
        while True:
            for AnswerUpdated in filter_wrapper.event_filter.get_new_entries():
                self.__handle_event(AnswerUpdated, filter_wrapper)
            await asyncio.sleep(poll_interval)

    def monitor(self):
        loop = asyncio.get_event_loop()
        try:
            for filter_wrapper in self.filters:
                asyncio.ensure_future(self.__monitor(filter_wrapper, 10))
            loop.run_forever()
        finally:
            loop.close()


if __name__ == "__main__":
    # BlockchainMonitor()
    BlockchainMonitor().monitor()
