//SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract Certificate {

    struct certificate_info {
        string name;
        string date_of_issue;
        bytes32 unique_id;
    }
    mapping(bytes32 => certificate_info) public certificates;
    mapping (string => bytes32) public recovery_data;

    bytes32[] public id_storage;
    // takes in the required credentials to build the certificate. 
    function build_certificate (string memory _name, string memory _date)public returns(bytes32) { 
        
        
        bytes32 unique = keccak256(abi.encodePacked(_name, _date, msg.sender));
        certificate_info memory new_certificate;
        new_certificate = certificate_info({name: _name, date_of_issue: _date, unique_id: unique});
        
        certificates[unique] = new_certificate;
        recovery_data[_name] = unique;
        return unique;
      
    }
    // uses the unique id to access the certificate details
    function access_certificate(bytes32 id) public view returns(certificate_info memory){
        return certificates[id];
    }

    function recover_certificate (string memory your_name) public view returns(bytes32, string memory){
        // if the certificate is lost
        string memory message = "use the id in the 'access_certificates' function to get back the lost credentials.";
        return (recovery_data[your_name], message);
    }
}
