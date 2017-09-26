#!/usr/bin/python

import sys
import os

java_file = sys.argv[1]

test_file_path = java_file.replace('/main/', '/test/', 1)
last_slash_idx = test_file_path.rfind('/') + 1
class_name = test_file_path[last_slash_idx:].replace('.java', '')
test_file_name = "Test" + test_file_path[last_slash_idx:]
test_class_name = test_file_name.replace('.java', '')
test_file_path = test_file_path[:last_slash_idx] + test_file_name
test_file_dir = test_file_path[:last_slash_idx]
package = test_file_dir[test_file_path.rfind('/java/')+6:].replace("/", ".")
package = package[:len(package)-1]

print "---------------------------------"
print "Java file: " + java_file
print "Test file: " + test_file_path
print "Test file dir: " + test_file_dir
print "Test file name: " + test_file_name
print "Test class name: " + test_class_name
print "Class name: " + class_name
print "Package: " + package
print "---------------------------------\n"

try:
	os.makedirs(test_file_dir)
except:
	print "File folder path exists, no need to create.\n"

f = open(test_file_path, 'w')

f.write("package " + package + ";\n\n")

f.write("import gr.interamerican.bo2.arch.exceptions.DataException;\n")
f.write("import gr.interamerican.bo2.arch.exceptions.LogicException;\n")
f.write("import gr.interamerican.bo2.impl.open.creation.Factory;\n")
f.write("import org.junit.*;\n\n")
f.write("import static org.mockito.Mockito.*;\n")
f.write("import static org.junit.Assert.*;\n\n")

f.write("/**\n");
f.write(" * " + class_name + " tests.\n");
f.write(" */\n");
f.write("public class " + test_class_name + " {\n\n")

f.write("\t/**\n");
f.write("\t * Test subject.\n");
f.write("\t */\n");
f.write("\t" + class_name + " sut = Factory.create(" + class_name + ".class);\n\n")

f.write("\t/**\n");
f.write("\t * Test class setup.\n");
f.write("\t */\n");
f.write("\t@BeforeClass\n")
f.write("\tpublic static void setup() {\n")
f.write("\t\t\n")
f.write("\t}\n\n")

f.write("\t/**\n");
f.write("\t * Test class tear down.\n");
f.write("\t */\n");
f.write("\t@AfterClass\n")
f.write("\tpublic static void tearDown() {\n")
f.write("\t\t\n")
f.write("\t}\n\n")

f.write("\t/**\n");
f.write("\t * Test setup.\n");
f.write("\t */\n");
f.write("\t@Before\n")
f.write("\tpublic void before() {\n")
f.write("\t\t\n")
f.write("\t}\n\n")

f.write("\t/**\n");
f.write("\t * Test tear down.\n");
f.write("\t */\n");
f.write("\t@After\n")
f.write("\tpublic void after() {\n")
f.write("\t\t\n")
f.write("\t}\n\n")

f.write("\t/**\n");
f.write("\t * foo() test.\n");
f.write("\t */\n");
f.write("\t@Test\n")
f.write("\tpublic void testFoo() {\n")
f.write("\t\t\n")
f.write("\t}\n\n")

f.write("}\n")
f.close()

print "=============================================\n"

f = open(test_file_path, 'r')
print f.read()



















