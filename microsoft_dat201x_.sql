
select Name as Product from SalesLT.Product;


select ProductId, Name, ListPrice, StandardCost, ListPrice - StandardCost as Margin, Color, Size
from SalesLt.Product;


select cast(ProductID as varchar(5)) + ': ' + Name as ProductName
from SalesLt.Product;

select CONVERT(varchar(5), ProductID) + ': ' + Name as ProductName
from SalesLt.Product;

-- Convert Dates
select SellStartDate, convert(nvarchar(30), SellStartDate) As ConvertedDate,
  convert(nvarchar(30), SellStartDate, 126) as ISO8601FormatDate
from SalesLt.Product;

-- Try to cast
select Name, TRY_CAST(Size as Integer) as NumericSize
from SalesLt.Product

--
select Name, ISNULL(TRY_CAST(Size as Integer),0) AS NumericSize
from SalesLt.Product

-- null strings changed to 'none entered'
select ProductNumber, ISNULL(Color, 'none entered') + ', ' + ISNULL(Size, 'none entered') as ProductDetails
from SalesLt.Product

-- find first non-null date
select Name, coalesce(DiscontinuedDate, SellEndDate, SellStartDate) as LastActivity
from SalesLt.Product


select Name,
   case
     when SellEndDate is NULL then 'On Sale'
	 else 'Discontinued'
   end as SalesStatus
from SalesLt.Product

-- Removes duplicates, only shows all colors
select distinct Color
from SalesLt.Product

-- 
select top 10 with ties Name, ListPrice
from SalesLt.Product
order by ListPrice desc;

--
select Name, ListPrice from SalesLt.Product order by ProductNumber offset 0 rows fetch next 10 rows only;

--
select distinct isnull(Color, 'none') as color from SalesLt.Product;

--Filtering with Predicates
select Name, Color, Size From SalesLt.Product where ProductModelID = 6;
--
select Name, Color, Size From SalesLt.Product where ProductNumber like 'FR%';
--
select ProductNumber, Name, Color, Size From SalesLt.Product where ProductNumber like 'FR-_[0-9][0-9]_-[0-9][0-9]';

select Name from SalesLt.Product where SellEndDate is not null;

select Name from SalesLt.Product where SellEndDate between '2006/1/1' and '2006/12/31';

select ProductCategoryID, Name, ListPrice from SalesLt.Product where ProductCategoryID in (5,6,7);

select ProductCategoryID, Name, ListPrice from SalesLt.Product where ProductCategoryID in (5,6,7) and SellEndDate is null;



-- Lab 2. Challenge 1. Question 1
select distinct City, StateProvince from SalesLt.Address;
-- Question2
select top 10 percent Weight, Name from SalesLt.Product order by Weight desc;
-- Question3
select Name, Weight from SalesLt.Product order by Weight desc offset 10 rows fetch next 100 rows only;

-- Lab 1. Challenge 2. Question 1
select * from SalesLt.Product;
select Name, Color, Size from SalesLt.Product where ProductModelID = 1;

-- Joins. Extend Columns from multiple tables.
select SalesLt.Product.Name as ProductName, SalesLT.ProductCategory.Name as Category
from SalesLt.Product
inner join SalesLt.ProductCategory
on SalesLt.Product.ProductCategoryID = SalesLt.ProductCategory.ProductCategoryID;

select SalesLt.Product.Name as ProductName, SalesLT.ProductCategory.Name as Category
from SalesLt.Product
inner join SalesLt.ProductCategory
on SalesLt.Product.ProductCategoryID = SalesLt.ProductCategory.ProductCategoryID;

select oh.OrderDate, oh.SalesOrderNumber, p.Name as ProductName, od.OrderQty, od.UnitPrice, od.SalesOrderID
from SalesLt.SalesOrderHeader as oh
inner join SalesLT.SalesOrderDetail as od
on od.SalesOrderID = oh.SalesOrderID
inner join SalesLT.Product as p
on od.ProductID = p.ProductID
order by oh.OrderDate, oh.SalesOrderID, od.SalesOrderDetailID;

--multiple join predicates
select oh.OrderDate, oh.SalesOrderNumber, p.Name as ProductName, od.OrderQty, od.UnitPrice, od.SalesOrderID
from SalesLt.SalesOrderHeader as oh
inner join SalesLT.SalesOrderDetail as od
on od.SalesOrderID = oh.SalesOrderID
inner join SalesLT.Product as p
on od.ProductID = p.ProductID and od.UnitPrice < p.ListPrice
order by oh.OrderDate, oh.SalesOrderID, od.SalesOrderDetailID;


--outer joins. All the employees AND the products the employees have sold
 -- left outer join -- retain all the rows from the table to the left
 -- full outer join -- reatin all the rows from both tables

 -- return only customers that haven't purchased anything
 select c.FirstName, c.LastName, oh.SalesOrderNumber
 from SalesLt.Customer as c
 left outer join SalesLt.SalesOrderHeader as oh
 on c.CustomerID = oh.CustomerID
 where oh.SalesOrderNumber is null
 order by c.CustomerID;

 select p.Name as ProductName, oh.SalesOrderNumber
 from SalesLt.Product as p
 left join SalesLt.SalesOrderDetail as od
 on p.ProductID = od.ProductID
 left join SalesLt.SalesOrderHeader as oh
 on od.SalesOrderID = oh.SalesOrderID
 order by p.ProductID;

 select p.Name as ProductName, c.Name as Category, oh.SalesOrderNumber
 from SalesLt.Product as p
 left outer join SalesLT.SalesOrderDetail as od
 on p.ProductID = od.ProductID
 left outer join SalesLt.SalesOrderHeader as oh
 on od.SalesOrderID = oh.SalesOrderID
 inner join SalesLt.ProductCategory as c
 on p.ProductCategoryID = c.ProductCategoryID
 order by p.ProductID;

--Use a Left Outer Join to include all rows from the first table and values from matched rows in the second table. Columns in the second table for which no matching rows exist are populated with NULLs.
--Use a Right Outer Join to include all rows from the second table and values from matched rows in the first table. Columns in the first table for which no matching rows exist are populated with NULLs.
--Use a Full Outer Join to include all rows from the first and second tables. Columns in the either table for which no matching rows exist are populated with NULLs.

-- Cross Joins. Cartesian Product
select p.Name, c.FirstName, c.LastName, c.Phone
from SalesLT.Product as p
cross join SalesLt.Customer as c;

--Self Join. Employee to their Manager
--select e.EmployeeName, m.EmployeeName as ManagerName
--from SalesLT.Employee as e
--left join SalesLT.Employee as m
--on e.ManagerID = m.EmployeeID

-- Union removes duplicate rows!!
-- UNION ALL - keeps duplicate
--select FirstName, LastName
--from SalesLT.Employees
--union
--select FirstName, LastName
--from SalesLT.Customers
--order by LastName;
-- Also alias 'Employee' as Type to make an identical row display twice.

-- Intersect -- Look for duplicates
-- Except returns only distinct rows that appear in the first set BUT NOT the second




--order by e.ManagerID;
select * from SalesLT.Customer;
select * from SalesLT.CustomerAddress;
select * from SalesLt.SalesOrderHeader;
select * from SalesLt.Address;
-- Lab 3. Challenge 1. Question 1
select c.CompanyName, ca.AddressType, a.AddressLine1, s.SalesOrderID, s.TotalDue
from SalesLt.Customer as c
inner join SalesLt.SalesOrderHeader as s
on c.CustomerID = s.CustomerID
inner join SalesLt.CustomerAddress as ca
on ca.CustomerID = s.CustomerID
inner join SalesLt.Address as a
on ca.AddressID = a.AddressID


select CompanyName, MainOffice from SalesLT.Customer;
select SalesOrderID, TotalDue from SalesLt.SalesOrderHeader;

select Name from s.SalesOrderID
from SalesLT.Customer as c
outer join SalesLT.SalesOrderHeader as s;


-- scalar - operate on a single row. return single value as output. year for example:
select year(SellStartDate) SellStartYear, ProductID, Name
FROM SalesLT.Product
order by SellStartYear;

select datediff(yy, SellStartDate, GETDATE()) YearsSold, ProductID, Name
from SalesLt.Product;

select concat(FirstName + ' ', LastName) as FullName
from saleslt.customer;

select Name, ProductNumber, substring(ProductNumber, charindex('-', ProductNumber) + 1, 4) as ProductType
from saleslt.product;

-- logical functions -- isnumeric -- iif(listprice > 50, 'high', 'low') <- choose high or low based on listprice
   -- choose (ProductCategoryID, 'Bikes, 'Components') will give ID > 2 a null value
select name, size as numericsize
from saleslt.product
where isnumeric(size) = 1;

select Name, iif(isnumeric(Size) = 1, 'Numeric', 'Non-Numeric') SizeType
from saleslt.product;

-- window functions. functions applied to set of rows. Includes ranking, offset, aggregate, and distribution functions
select top(100) ProductID, Name, ListPrice,
  rank() over(order by ListPrice desc) as RankByPrice
from SalesLT.Product as p
order by RankByPrice;

select c.Name as category, p.name as product, listprice,
  rank() over(partition by c.name order by listprice desc) as rankbyprice
from saleslt.product as p
join saleslt.productcategory as c
on p.productcategoryid = c.productcategoryid
order by category, rankbyprice

-- aggregate functions
select count(*) as products, count(distinct ProductCategoryID) as Categories, avg(ListPrice) as AverageListPrice
from saleslt.product;

-- grouping aggregated data
select c.Salesperson, isnull(sum(oh.SubTotal), 0.00) SalesRevenue
from saleslt.customer as c
left join SalesLT.SalesOrderHeader as oh
on c.CustomerID = oh.CustomerID
group by c.Salesperson
order by SalesRevenue desc;

-- filtering aggregated data
-- having clause is processed after group by -- where is processed before group by
select ProductID, sum(sod.OrderQty) as quantity
from SalesLt.SalesOrderDetail as sod
join saleslt.salesorderheader as soh
on sod.SalesOrderID = soh.SalesOrderID
where year(soh.OrderDate)=2008
group by ProductID
having sum(sod.orderqty)>50

-- subqueries.. maximum 
select max(unitprice) from SalesLT.SalesOrderDetail

select * from SalesLt.Product
where ListPrice > (select max(unitprice) from SalesLT.SalesOrderDetail)
-- correlated subqueries
-- refer to elements of tables used in outer query. for each row in outer query, run subquery
select CustomerID, SalesOrderID, OrderDate
from SalesLT.SalesOrderHeader as So1
order by CustomerID, OrderDate

select CustomerID, SalesOrderID, OrderDate
from SalesLT.SalesOrderHeader as So1
where orderdate = (select max(orderdate) from SalesLT.SalesOrderHeader)

select CustomerID, SalesOrderID, OrderDate
from SalesLT.SalesOrderHeader as So1
where orderdate = (select max(orderdate) 
from SalesLT.SalesOrderHeader as So2
where So2.CustomerID = So1.CustomerID)
order by CustomerID

--apply operator
-- cross apply similar to cross join - for each row
-- outer apply like lefter outer join -- adds rows for those with null columns in right table
 select soh.salesorderID, MUP.MaxUnitPrice
 from SalesLT.SalesOrderHeader as soh
 cross apply saleslt.udfMaxUnitPrice(soh.SalesOrderID) as mup
 order by soh.salesorderID
-- runs for each sales order header the maximum unit price

--Table Expressions
-- Views are named queries with definitions stored in a database
   -- provide abstractions and security layer for database. Give them rights to view instead of underlying table
create view SalesLT.vCustomerAddress

-- temporary table -- scope to the session
-- Temporary tables are prefixed with a # symbol and stored in a temporary workspace (the tempdb database in SQL Server).
-- Excessive use of temporary tables can negatively affect overall database server performance.
create table #tmpProducts
-- temp results sets with # prefix -- global temperoary tables are created with ## prefix
-- Table Variables - introduced 


-- table variable -- scope to batch.. till semicolon
-- Table variables are prefixed with a @ symbol and are stored in memory.
-- use on very small datasets
declare @varProducts table

-- Tabled values functions
-- function that retuns a table -- permanently lives in database -- support input parameters
-- pass values into function
create function SalesLt.fn_getOrderItems 
(@City as varchar(20))
returns table
as
return
(select C.customerID, FirstName, LastName, AddressLine1, City, StateProvince
 from salesLt.Customer as C join SalesLT.CustomerAddress as CA
 on C.CustomerID=CA.CustomerID
 join SalesLt.Address as A on CA.AddressID=A.AddressID
 where City=@City);
 -- stored in Programmability / Functions / Table Values functions

 select * from SalesLt.fn_getOrderItems('Bellevue')


-- derived tables are subqueries
-- virtual tables -- within query
-- use internal or external aliases -- 
select orderyear, count(distinct custid) as cust_count
from ( select year(orderdate) as orderyear, custid
    from sales.orders) as derived_year
group by orderyear;

-- or externally
select orderyear, count(distinct custid) as cust_count
from (select year(orderdate), custid
    from sales.orders) as 
	derived_year(orderyear, custid)
group by orderyear

select category, count(productID) as Products
from
  (select p.ProductID, p.Name as Product, c.Name as Category
   from salesLt.product as p
   join saleslt.productCategory as c
   on p.productCategoryID =c.ProductCategoryID) as ProdCats
   group by Category
   order by Category;

-- common table expressions
with CTE_year(OrderYear, CustID)
as
(
  select year(orderdate), custid
  from sales.orders
)
select OrderYear, count(distinct CustID) as Cust_Count
from CTE_Year
group by orderyear;

-- levels of aggregation
-- grouping sets builds on group by
select employeeID, customerID, sum(amount) as totalAmount
from Sales.SalesOrder
group by
grouping sets(EmployeeID, customerID, ()); -- () is grand total
-- null null will be total for all sales
-- null 1 -- subtotal for each customer
-- 1 null -- subtotal for each employee
----- problem is null could come from source data
-- grouping_id function provides method to mark a row with 1 or 0 to indentify which grouping set per row
select cat.ParentProductCategoryName, cat.ProductCategoryName, count(prd.ProductID) as Products
from SalesLt.vGetAllCategories as cat
left join SalesLT.Product as prd
on prd.ProductCategoryID = cat.ProductCategoryID
group by cat.ParentProductCategoryName, cat.ProductCategoryName

-- grouping sets
select cat.ParentProductCategoryName, cat.ProductCategoryName, count(prd.ProductID) as Products
from SalesLt.vGetAllCategories as cat
left join SalesLT.Product as prd
on prd.ProductCategoryID = cat.ProductCategoryID
group by grouping sets(cat.ParentProductCategoryName, (cat.ParentProductCategoryName, cat.ProductCategoryName), ())
order by cat.ParentProductCategoryName, cat.ProductCategoryName;

-- rollup provides shortcut for defining grouping sets with combinations 
select cat.ParentProductCategoryName, cat.ProductCategoryName, count(prd.ProductID) as Products
from SalesLt.vGetAllCategories as cat
left join SalesLT.Product as prd
on prd.ProductCategoryID = cat.ProductCategoryID
group by rollup (cat.ParentProductCategoryName, cat.ProductCategoryName)
order by cat.ParentProductCategoryName, cat.ProductCategoryName;

-- cube provides shortcut for all possible combinations
select cat.ParentProductCategoryName, cat.ProductCategoryName, count(prd.ProductID) as Products
from SalesLt.vGetAllCategories as cat
left join SalesLT.Product as prd
on prd.ProductCategoryID = cat.ProductCategoryID
group by cube (cat.ParentProductCategoryName, cat.ProductCategoryName)
order by cat.ParentProductCategoryName, cat.ProductCategoryName;


-- pivoting data
-- from rows-based orientation to a columns based orientation. may include aggregation
-- really useful for reports

-- unpivot data
-- won't get all back 

select Name ProductName, ListPrice + try_convert(money, Size) as Total from SalesLT.Product

select Name + ' ' + NULLIF(Size,'') from SalesLT.Product;

select * from SalesLT.Customer

-- select into <- select into a table
-- @@IDENTITY - last identity generated in this session. This connection, which identity. Insert Order includes order details -- orderDetail is @@Identity not UserID
-- SCOPE_IDENTITY() last identity generated in current scope of query. Problem with multiple tables. Best within transaction
-- IDENT_CURRENT('<table_name>'): last identity inserted into a table. Across all sessions, so you might get somebody else's
isert into Sales.Orders (CustomerID, Amount)
values
(12, 205.9);
select scope_identity() as OrderID;

-- sequences generate sequential numbers
-- select next value for
create sequence Sales.OrderNumbers as INT
starts with 1 increment by 1;
select next value for Sales.OrderNumbers;


create table SalesLT.CallLog
(
  CallID int IDENTITY PRIMARY KEY NOT NULL,
  CallTime datetime NOT NULL DEFAULT GETDATE(),
  SalesPerson nvarchar(256) NOT NULL,
  CustomerID int NOT NULL REFERENCES SalesLT.Customer(CustomerID),
  PhoneNumber nvarchar(25) NOT NULL,
  Notes nvarchar(max) NULL
);
GO
insert into SalesLT.CallLog (SalesPerson, CustomerID, PhoneNumber)
values
('adventure-works\jillian0', 3, '295-345-1234');


insert into SalesLT.DebugTable4
values
('Feb', 22165, 38779, 29079)


insert into SalesLT.CallLog (SalesPerson, CustomerID, PhoneNumber, Notes)
select SalesPerson, CustomerID, Phone, 'Sales promotion call'
from SalesLT.Customer
where companyName = 'Big-Time Bike Store';

select * from SalesLT.CallLog

-- USE UPDATE AND MERGE TO UPDATE DATA IN DATABASE
-- Update Product table -- new prices
update SalesLT.Product
set unitprice = (unitprice * 1.04)
where categoryid = 1 and discontinued = 0;

-- merge modifies based on a condition
-- P is production -- Staging is S
merge into Production.Products as P
  using Production.ProductStaging as S
  on P.ProductID = S.ProductID
when matched then
  update set
  p.UnitPrice = S.UnitPrice, P.Discontinued=S.Discontinued
when not matched then
  insert (Product, Category, UnitPrice)
  values(S.Prouct, Category, UnitPrice) 


-- truncate table clears entire table. Quicker
-- delete from Sales.LT deletes everything

----------------------------------------------
-- Batches are sets of commands sent to SQL Server as a unit
-- determine variable scope name resolution
-- use the GO keywork but not a T-SQL Command!
declare @color nvarchar(15)='Black', @size nvarchar(5)='L';
set @color = 'Blue';
print @color;
select * from Production.Product
where color=@color and Size=@size;
GO -- go is at end of batch. after this, variable is out of scope


-- Typically a view is like a table
-- stored procedures -- set up to use parameters
create procedure saleslt.GetProductsByCategory (@CategoryID INT = NULL)
AS
IF @CategoryID IS NULL
  SELECT ProductID, Name, Color, Size, ListPrice
  FROM SalesLT.Product
ELSE
  SELECT ProductID, Name, Color, Size, ListPrice
  FROM SalesLT.Product
  WHERE ProductCategoryID = @CategoryID;

-- run a stored procedure like this:
EXEC SalesLT.GetProductsByCategory 6


-- Errors --
if @@RoWCOUNT < 1
  THROW 50001, 'Product not found', 0;

