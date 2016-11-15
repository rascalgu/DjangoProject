SELECT * FROM testtool.testtools_category;
select * from testtool.testtools_category where x >= 0;
select * from testtool.testtools_category where x = 1 and y > 0;
select * from testtool.testtools_category where x = 2 and y > 0;
select id,category_name from testtool.testtools_category group by x,y;

testtools_project
select * from testtool.testtools_interface;


UPDATE testtool.testtools_interface SET request_link=REPLACE(request_link,'http"//www','http://test');

update testtool.testtools_interface set request_sample = replace(request_sample,'dev','test');

SET SQL_SAFE_UPDATES = 0;