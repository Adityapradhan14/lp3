// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    // Structure for student
    struct Student {
        uint rollNo;
        string name;
        uint marks;
    }

    // Array to store multiple students
    Student[] public students;

    // Add new student
    function addStudent(uint _rollNo, string memory _name, uint _marks) public {
        students.push(Student(_rollNo, _name, _marks));
    }

    // Get total students count
    function getCount() public view returns (uint) {
        return students.length;
    }

    // Get student details by index
    function getStudent(uint index) public view returns (uint, string memory, uint) {
        require(index < students.length, "Invalid index");
        Student memory s = students[index];
        return (s.rollNo, s.name, s.marks);
    }

    // Fallback function - gets triggered when someone sends ether or invalid call
    fallback() external payable {
        // You can log this or store info if needed
    }

    // To receive Ether directly
    receive() external payable {}
}

