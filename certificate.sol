//SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract Certificate {

    struct certificate_info {
        string name;
        string date_of_issue;
        bytes32 unique_id;
        string web3StorageUrl;
    }
    mapping(bytes32 => certificate_info) certificates;
    mapping (string => bytes32) public recovery_data;

    // takes in user's name and current date to build the certificate. returns a unique id
    // which is used to access the certificate data in the 'access_certificates' function below
    function build_certificate (string memory _name, string memory _date, string memory _web3StorageUrl)external returns(bytes32) {
        bytes32 unique = keccak256(abi.encodePacked(_name, _date, msg.sender));
        certificate_info memory new_certificate;
        new_certificate = certificate_info({name: _name, date_of_issue: _date, unique_id: unique, web3StorageUrl:_web3StorageUrl});
        
        certificates[unique] = new_certificate;
        recovery_data[_name] = unique;
        return unique;
      
    }
    // takes in the unique id and returns the certificate credentials
    function access_certificate(bytes32 id) external view returns(certificate_info memory){
        return certificates[id];
    }

    // takes in user's name and returns the certificate details
    function recover_certificate (string memory your_name) external view returns(string memory, certificate_info memory){
        // if the certificate is lost
        string memory message = "Certificate recovered!";
        return (message, certificates[recovery_data[your_name]]);
    }
}
