from OOB_2_imported import Base

class Derived(Base):
	def bar(self):
		return 'bar'

d = Derived()
print(d.bar())
print(d.foo())
