# file_has_not_been_modified.py
This script is intended to be used as HEALTHCHECK CMD, in case a running container relies on always using an up-to-date
version of a file.

On its first execution the script will create a hash-file, that contains a hash of the real file. Then at each
subsequent execution the hash of the file will be compared against the stored one. The script will return with an error
code != 0 in case the stored hash and the file has differ or in case of any IOError.
