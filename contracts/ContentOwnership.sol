// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ContentOwnership {
    struct Content {
        address owner;
        uint256 timestamp;
    }

    mapping(bytes32 => Content) public contents;

    event ContentRegistered(bytes32 indexed contentHash, address indexed owner, uint256 timestamp);

    function registerContent(bytes32 contentHash) public {
        require(contents[contentHash].owner == address(0), "Content already registered.");
        
        contents[contentHash] = Content({
            owner: msg.sender,
            timestamp: block.timestamp
        });
        
        emit ContentRegistered(contentHash, msg.sender, block.timestamp);
    }

    function getContentOwner(bytes32 contentHash) public view returns (address owner, uint256 timestamp) {
        require(contents[contentHash].owner != address(0), "Content not registered.");
        return (contents[contentHash].owner, contents[contentHash].timestamp);
    }
}
