indian_dummy_names = [
    "Aarav Sharma", "Veda Iyer", "Ishaan Patel", "Saanvi Kapoor", "Aditya Reddy",
    "Ananya Gupta", "Vikram Mehta", "Priya Rao", "Arjun Desai", "Neha Verma",
    "Rohit Singh", "Sneha Joshi", "Karan Shah", "Pooja Malhotra", "Sameer Agarwal",
    "Shreya Jain", "Rahul Yadav", "Kritika Choudhury", "Amit Kumar", "Rina Nair",
    "Ravi Mishra", "Tanya Kapoor", "Manish Gupta", "Swati Sharma", "Vishal Bhat",
    "Ayesha Khan", "Deepak Patil", "Tanvi Agarwal", "Siddharth Reddy", "Aarti Mehta",
    "Ankur Prasad", "Madhavi Rao", "Puneet Sharma", "Maya Verma", "Anil Kapoor",
    "Disha Patel", "Yash Rajput", "Kiran Das", "Divya Joshi", "Rajesh Saini",
    "Pallavi Singh", "Raghav Gupta", "Simran Bedi", "Nikhil Deshmukh", "Kavya Saxena",
    "Himanshu Kumar", "Neelam Kapoor", "Gaurav Tiwari", "Rekha Yadav", "Suman Nair"
]


names_start_with_A = len([name for name in indian_dummy_names if name.startswith("A")])
print(f"Names starting with A: {names_start_with_A}")


total_names = len(indian_dummy_names)
print(f"Total number of names:{total_names}")

print("surnames :")
for name in indian_dummy_names:
  surname = name.split()[-1]
  print(surname)





print("Names starting with Y:")
for name in indian_dummy_names:
    if name.startswith("Y"):
        print(name)




print("Names ending with 'a':")
for name in indian_dummy_names:
    if name.endswith("a"):
        print(name)




print("All names in capital letters:")
for name in indian_dummy_names:
    print(name.upper())

