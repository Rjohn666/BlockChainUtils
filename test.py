from hdwallet import HDWallet
from hdwallet.symbols import BTC

# 你的 xprv 扩展私钥
xprv = ''

# 创建 HDWallet 实例
hdwallet = HDWallet(symbol=BTC)

# 导入 xprv 扩展私钥
hdwallet.from_xprivate_key(xprv)

# 获取私钥
hdwallet.from_path(path='''m/86'/0'/0'/0/1713267002''')
private_key = hdwallet.private_key()

print(private_key)