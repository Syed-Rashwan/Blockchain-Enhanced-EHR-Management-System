// SPDX-License-Identifier: MIT
// contracts/EHR.sol
pragma solidity ^0.8.0;

contract EHR {
    struct Record {
        string patientId;
        string dataHash;
        address doctor;
        bool isShared;
    }

    mapping(uint => Record) public records;
    uint public recordCount;

    function addRecord(string memory _patientId, string memory _dataHash) public {
        recordCount++;
        records[recordCount] = Record(_patientId, _dataHash, msg.sender, false);
    }

    function shareRecord(uint _recordId) public {
        require(msg.sender == records[_recordId].doctor, "Only the doctor can share this record");
        records[_recordId].isShared = true;
    }
}