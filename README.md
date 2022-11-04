## Как запусить 
1. В файле spec.yaml нужно указать 
* Ваш alchemy_url 
* Пары, которые нужно мониторить, и адреса оракулов, события с которых хотите обрабатывать.

    Пример
    ```yaml
    connection_settings:
      alchemy_url: 'https://eth-mainnet.g.alchemy.com/v2/MY_KEY'
    currency_pairs:
      - ETH/USD:
          oracles_addresses:
            - '0x37bC7498f4FF12C19678ee8fE19d713b87F6a9e6'
      - LINK/ETH:
          oracles_addresses:
            - '0xbba12740DE905707251525477bAD74985DeC46D2'
      - USDT/ETH:
          oracles_addresses:
            - '0x549aE844Ab6B4a6Eb466F98dFFbc1FC9224e316d'
    ```
2. Для установки всех нужных зависимостей нужно вызвать команду
```shell
pip install -r requirements.txt
```
3. Запустить мониторинг командой
```shell
python monitor.py
```

## Пример вывода в лог
```
2022-11-04 15:27:28,311 - ETH/USD - Start monitor pair ETH/USD. Oracle address: 0x37bC7498f4FF12C19678ee8fE19d713b87F6a9e6
2022-11-04 15:27:28,497 - LINK/ETH - Start monitor pair LINK/ETH. Oracle address: 0xbba12740DE905707251525477bAD74985DeC46D2
2022-11-04 15:27:28,685 - USDT/ETH - Start monitor pair USDT/ETH. Oracle address: 0x549aE844Ab6B4a6Eb466F98dFFbc1FC9224e316d
2022-11-04 15:32:55,386 - ETH/USD - Price changes in pair ETH/USD. Oracle address: 0x37bC7498f4FF12C19678ee8fE19d713b87F6a9e6. Current price: 158350000000, block number: 15896673, tx hash: 0x4fbb9a61a92680ed573dc35b1c79df54d8c26d8b5c450e10e4a3fa108a832d02
2022-11-04 15:33:26,512 - USDT/ETH - Price changes in pair USDT/ETH. Oracle address: 0x549aE844Ab6B4a6Eb466F98dFFbc1FC9224e316d. Current price: 73521588, block number: 15896676, tx hash: 0xa629c4210c585ba90a8fb069ba9782db2162fb741c24b0f6e81041009748cb44
2022-11-04 15:35:59,858 - USDT/ETH - Price changes in pair USDT/ETH. Oracle address: 0x549aE844Ab6B4a6Eb466F98dFFbc1FC9224e316d. Current price: 73632276, block number: 15896688, tx hash: 0xc4d6602f7853bbddcae09e806f8be169d4bc193fbe7574fe26c06051defd005a
2022-11-04 15:37:11,030 - ETH/USD - Price changes in pair ETH/USD. Oracle address: 0x37bC7498f4FF12C19678ee8fE19d713b87F6a9e6. Current price: 159699000000, block number: 15896694, tx hash: 0xfc41a7d0893a8f55c0733bb57e288056b85ed972d492bfd96b9d7d519bb4a190
```