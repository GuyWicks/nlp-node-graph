from pyvis.network import Network


def test_1():
    net = Network(height="750px", width="100%", bgcolor="#eeeeee", font_color="white")
    net.add_node(0,image="person.gif")
    net.add_node(1,shape="box",label="hello\n[type]",color="green",size=60)
    net.add_node(3,size=9)
    net.add_edge(0,3)
    net.add_edge(0,1,label="connected")
    net.write_html("test.html",notebook=False)
