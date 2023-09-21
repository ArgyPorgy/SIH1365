//SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract Certificate {

    struct certificate_info {
        string name;
        string date_of_issue;
        bytes32 unique_id;
    }
    
    mapping(bytes32 => certificate_info) public certificates;


    function build_certificate (string memory _name, string memory _date)public {
        
        
        bytes32 unique = keccak256(abi.encodePacked(_name, _date, msg.sender));
        
        certificate_info memory new_certificate;
        new_certificate = certificate_info({name: _name, date_of_issue: _date, unique_id: unique});
        
        certificates[unique] = new_certificate;
      
    }
    function access_certificate(bytes32 id) public returns(string memory, string memory, bytes32){
        certificate_info memory val = certificates[id];
        return (val.name, val.date_of_issue, val.unique_id);
    }
    



}
