# ***filecached***
## **About**
*filecached* is a very simple KVS server.

This name respecting to *memcached*, but its not like *memcached*.

*filecached* is saving entries to each files, and leave reliability and caching to filesystem.

## ***This is Experimental.***

## **Usage**
### *Find*
Exactly one
```
> a
a=1
```
Show all
```
> _
a=1
b=2
c=3
d=4
```
`_` is special character for show all entry.
Its only affect exact hit.
### *Insert/Update*
```
> e=5
e
> _
a=1
b=2
c=3
d=4
e=5
```
```
> a=6
a
> _
a=6
b=2
c=3
d=4
e=5
```
### *Delete*
```
> e=
e
> _
a=6
b=2
c=3
d=4
```
