# jsonnavigator
Need a tool to jump around JSON-generated data strucutres relatively easily.
The structures are a mix of dicts and lists in Python.

pain points
-----------
* cumbersome to write a series of square bracket addresses
* since the dicts are not defaultdicts, reaching for a missing key causes an exception. need to use get(), BUT using get gets clunky if we are reaching deeper: json_response['result'].get('person',{}).get('name','N/A'); what if we need an element of a dict from a list, but the list is empty (i.e. is there a get()-like method for lists)?
	* would want to return None or some default value when there is a missing key/element along the navigation path
* it would be useful to be able to fetch dicts that contain particular key-value pairs. e.g. from a list of dicts get those dicts where message_type:image, it's difficult to succinctly get to such a pair and then to go back to the other dict entries associated with it. (!!! need to make this a stable filter, to allow later slicing consistent with source order in the list, shouldn't be too hard - just start at the beginning)
	* FOR NOW pass a a two-element tuple with the key and the value.
	* LATER, for this we could pass a dict like this json.navigate('messages',{'message_type':'image'})
		* if we are looking for several possible values of a key, pass dict with list/tuple/set like this json.navigate('messages','{'message_type':['image','text']})
		* and if more key-value pairs should be examined in the filter, just make so in the dict json.navigate('messages',{'message_type':'image', 'sender':'John'}) TBD

the following converges on just passing slices
* would be nice to be able to fetch all elements with a particular key from a list
* would be nice to have wildcards json.navigate('result', '*', 'name'). This is pretty much the same as  the point above
	* seems smart to define some constants like ALL to be able to pass that instead of the string asterisk. or use the ellipsis (...) to denote ALL
	* then we can have a switch to turn string wildcards on or off when initializing, or in context manager (as soon as I can wrap my head around those).
* Nice to be able to get a slice of a list when declaring the navigation path json.navigate('result','[2:7]'); It seems like a good idea to accept python slice objects for this.

* would be nice to have control of the depth json.navigate('result','*2'); Do we preserve some nesting in returned result? or maybe add some metadata on depth of an element found? TBD
* Related to the above: do we allow wildcards to reach across levels? What would be path symbol for that? TBD
