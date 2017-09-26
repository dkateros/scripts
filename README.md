# Some quality of life scripts
## codegen
Because we hate boilerplate.
### java-ut (Java unit test generator)
Assumes a default maven layout. Uses Junit4 and Mockito. Tested with Python 2.7.12.
1. createTestFile.sh: takes a single argument, that is hopefully the name of the class you want to generate a unit test skeleton for. Finds the java file within the working directory. Feeds this file to ctf.py that does most of the heavy lifting.
1. ctf.py: Creates a test class skeleton in the same package. Start your unit test from this skeleton :)

```java
package gr.dkateros.demo.javaut;

import gr.interamerican.bo2.arch.exceptions.DataException;
import gr.interamerican.bo2.arch.exceptions.LogicException;
import gr.interamerican.bo2.impl.open.creation.Factory;
import org.junit.*;

import static org.mockito.Mockito.*;
import static org.junit.Assert.*;

/**
 * Foo tests.
 */
public class TestFoo {

	/**
	 * Test subject.
	 */
	Foo sut = Factory.create(Foo.class);

	/**
	 * Test class setup.
	 */
	@BeforeClass
	public static void setup() {
		
	}

	/**
	 * Test class tear down.
	 */
	@AfterClass
	public static void tearDown() {
		
	}

	/**
	 * Test setup.
	 */
	@Before
	public void before() {
		
	}

	/**
	 * Test tear down.
	 */
	@After
	public void after() {
		
	}

	/**
	 * foo() test.
	 */
	@Test
	public void testFoo() {
		
	}

} 
```
