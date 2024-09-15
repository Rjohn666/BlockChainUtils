from hdwallet import HDWallet
from hdwallet.symbols import BTC

# 你的 xprv 扩展私钥
xprv = 'xprv9s21ZrQH143K2Lku5GEoqhb1Z2mYyM8132fi1rit12UFZvFqhCKwEV37d27ztc4JgprEWXfxQPDadJU3MAEPL6WqwqMxteXjUqp4Lx9BSPA'

# 创建 HDWallet 实例
hdwallet = HDWallet(symbol=BTC)

# 导入 xprv 扩展私钥
hdwallet.from_xprivate_key(xprv)

# 获取索引 0 私钥
hdwallet.from_path(path='''m/86'/0'/0'/0/1713267002''')
private_key = hdwallet.private_key()

print(private_key)