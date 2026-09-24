#Predicted output:
#['python', 'testing']
#False
#True

#.copy() creates a shallow copy: it makes a brand new dictionary object,
#so the dictionary itself (profile vs. updated) are different objects.
#However, .copy() does NOT create new copies of the values inside the
#dictionary. The "tags" list is a mutable object, and both the original
#and updated dictionaries end up holding a reference to the exact same
#list in memory. So when updated["tags"].append(tag) runs, it modifies
#the one shared list, which is why original["tags"] also shows the
#new tag, even though original was never directly changed.
#EXAMPLE:
Before:  original["tags"] = ["python"]
         updated["tags"]  = ["python"]     (same list, shared!)

After append("testing"):
         original["tags"] = ["python", "testing"]   ← changed too!
         updated["tags"]  = ["python", "testing"]   (still the same shared list)