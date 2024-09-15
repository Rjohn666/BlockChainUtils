# -*- coding: utf-8 -*-

import asyncio
import glob
import os
import random
import sys
import binascii

import loguru

sys.path.append("..")

from bcutils.btc.ordinals import (
    setup,
    ordi_mint,
    brc20_mint, ordi_mint_img,build_commit_privkey,build_reveal_privkey
)

def get_svg_strings(directory,count=10):
    # 使用 glob 模块获取目录下所有 SVG 文件
    svg_files = glob.glob(os.path.join(directory, '*.svg'))

    # 随机选择指定数量的 SVG 文件
    random_svg_files = random.sample(svg_files, count)

    # 读取选中的 SVG 文件内容并返回
    svg_strings = []
    for svg_file in random_svg_files:
        with open(svg_file, 'r', encoding='utf-8') as f:
            svg_strings.append(f.read())
    return svg_strings

    # 示例用法



def spilt_img_push_data(svg_text):
    pushdata = binascii.hexlify(svg_text.encode()).decode()
    # 分割成数组
    pushdata_array = []
    start = 0
    while start < len(pushdata):
        end = start + 1040
        if end > len(pushdata):
            end = len(pushdata)
        pushdata_array.append(pushdata[start:end])
        start = end
    return pushdata_array


async def main():
    """
    1. 修改testnet为False
    2. mnemonic: 用于生成在mint过程中需要commit address和reveal address
        * 空: 会随机生成，请保存好运行过程中黄色的日志，防止运行报错时召回资产
        * 你自己地址的助记词: 保存好黄色日志中Path数据
    3. receive_address: 铭文接收地址
    """

    testnet = False
    mnemonic = ""
    receive_address = "bc1pje7eu9m4htsqref4q5v8mfkf3vzmthgdjdhpj8axs3fwut5qay4s9amhuf"
    setup(testnet, mnemonic=mnemonic)


    img_list = get_svg_strings('./svgs',20)
    print(img_list)
    img_push_data = [
        spilt_img_push_data(i) for i in img_list
    ]



    txs = await ordi_mint_img(receive_address, pushdata_list=img_push_data, gas=5000)


    # txs = await brc20_mint(receive_address, brc20, amount, 20, gas=500)



if __name__ == "__main__":
    loguru.logger.add('logs/inscription.log', rotation="1 day",enqueue=True)
    asyncio.run(main())



