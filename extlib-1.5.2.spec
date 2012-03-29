@1

package "extlib" {
  version     = "1.5.2"
  description = "http://ocaml-extlib.googlecode.com/svn/doc/apiref/index.html"
  urls = [ "http://ocaml-extlib.googlecode.com/files/extlib-1.5.2.tar.gz" ]
  patches = [
   "local://files/extlib.install";
   "local://files/extlib.ocp"
  ]
  make = [ "ocp-build -init -scan" ]
}