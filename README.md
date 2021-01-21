# yiimp python library and command line api

Dependacy
* requests
* fire

To install dependencies run following line your favorite shell console

    pip install requests
    pip install fire 
    
    
## Optional parameter:
Following parameter are optional.

    --pool=
    
* default url: 
    * http://api.zergpool.com:8080


## Library usage:
yiimp library is contained in file `yiimp.py`.

Code snipplet for public api.

    import yiimp 
    
    pool = 'http://api.zergpool.com:8080'
    
    public_api = yiimp.PublicApi(pool)
    
    get_status = public_api.get_status()
    print(get_status)
  

## Command line usage:
`yiimp.py` can be used as commad line tools.

Usage:

    python yiimp.py get_status
    python yiimp.py get_currencies
    python yiimp.py get_blocks
    python yiimp.py get_miners
    python yiimp.py get_blocks_coin --sym=DGB
    python yiimp.py get_wallet --wallet=WALLET_ADDRESS
    python yiimp.py get_walletEx --wallet=WALLET_ADDRESS
   
Written by bitfawkes

donation:

    BTC:   3P1Aa3V1LQgF8zPsMXBzJ7N43RC13NhRnP
    BCH:   bitcoincash:qq0ggxmhfvdk8ekaerraz9fpehz57lklps6c8sefdn
    BCHA:  bitcoincash:qq0ggxmhfvdk8ekaerraz9fpehz57lklps6c8sefdn
    BCHSV: 13nMXjMdrd3xnDE5b196wN8dQUgEa3Xm3p
    ETH:   0x7326d593423515e51242b992d16e69aff6533ee5
    LTC:   M9PcgKeDzdRegeqwko1YCaPR4UYxxdAqUF
    DGB:   DHkt5Vd3GtA1cNr87TdpSMUKVMz634rjeP
    
