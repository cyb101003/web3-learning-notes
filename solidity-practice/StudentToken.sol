// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// 简单ERC20代币合约
// 作者：陈宇博 (Chen Yubo)
// 开发时间：2026.03

contract StudentToken {
    // 代币基本信息
    string public name = "ChenYubo Token";
    string public symbol = "CYB";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // 余额映射
    mapping(address => uint256) public balanceOf;

    // 转账事件
    event Transfer(address indexed from, address indexed to, uint256 value);

    // 构造函数：部署时给部署者mint 100万代币
    constructor() {
        totalSupply = 100 * 10**uint256(decimals);
        balanceOf[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // 转账函数
    function transfer(address to, uint256 value) public returns (bool) {
        require(balanceOf[msg.sender] >= value, "余额不足");
        require(to != address(0), "地址不能为0");

        balanceOf[msg.sender] -= value;
        balanceOf[to] += value;

        emit Transfer(msg.sender, to, value);
        return true;
    }
}
