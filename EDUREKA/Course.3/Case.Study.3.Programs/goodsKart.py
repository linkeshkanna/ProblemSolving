"""
Case Study:
Domain –E-Commerce
focus –Optimization
Business challenge/requirement
GoodsKart—largest ecommerce company of Indonesia with revenue of $2B+ acquired another ecommerce company FairDeal.
FairDeal has its own IT system to maintain records of customer, sales etc.
For ease of maintenance and cost savings GoodsKart is integrating customer databases of both the organizations hence customer data of FairDeal has to be converted in GoodsKartCustomer Format.

Key issues:
GoodsKart customer data has more fields than in FairDeal customer data.
Hence FairDeal data needs to be split and stored in GoodsKart Customer Object Oriented Data Structure

Considerations:
System should convert the data at run time

Data volume-NA
Additional information-NA

Business benefits:
GoodsKart can eventually sunset IT systems of FairDeal and reduce IT cost by 20-30% 

Approach to Solve:
Read FairDealCustomerData.csv
Name field contains full name –use regular expression to separate title, first name, last name
Store the data in Customer Class
Create Custom Exception – CustomerNotAllowedException
Pass a customer to function "createOrder" and throw CustomerNotAllowedExceptionin case of blacklisted value is 1

Enhancements for code:
Change function createOrder to take productname and product code as input
Create Class OrderReturn object of type Order in case customer is eligible
"""
