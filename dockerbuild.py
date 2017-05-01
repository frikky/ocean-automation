class docker_build(object):
    def __init__(self):
        pass
    
    # Verify if conf_file exists
    def generate_dockerfile(self, conf_file, ports=[]):
        if not ports or not isinstance(ports, list): 
            print "Ports not defined for Dockerfile generation"
            exit()

        depencies = ["git", "libevent-dev", "libdumbnet-dev", \
            "libpcap-dev", "libpcre3-dev", "libedit-dev", "bison", \
            "flex", "libtool", "automake", "zlib1g-dev", "make"]

        docker_config = ["FROM python:2.7-slim\n",
            "WORKDIR /app",
            "ADD %s" % conf_file,
            "ADD honeypots/Honeyd/ /app\n",
            "RUN apt-get update",
            "RUN %s" % " ".join(depencies),
            "RUN mv configure.in configure.ac",
            "RUN ./autogen.sh",
            "RUN ./configure",
            "RUN make",
            "RUN make install\n"]

        for items in ports:
            docker_config.append("EXPOSE %s" % str(items))
        docker_config.append("\nCMD [\"honeyd\", \"-d\", \"-f\", \"%s\"]" % conf_file)

        print "Saved to honeypots/Dockerfile" 
        self.write_file("honeypots/Dockerfile", docker_config)

    def generate_honeypot(self, ports, personality="Microsoft Windows XP Professional SP1", \
        distro="windows", mac="00:00:24:ab:8c:12", ip="172.17.0.20", \
        tcp="block", udp="block", icmp="block", filename="honeypot.conf"):
        if not ports or not isinstance(ports, list): 
            print "Ports not defined for honeypot generation."
            exit()

        print "Setting up honeypot config using the following config:"
        if distro.lower() == "windows": 
            print "Default: to Windows XP SP1"

        print "Using:\ntcp:%s\nudp:%s\nicmp:%s\n" % (tcp, udp, icmp)
        honeypot_config = ["create %s" % distro,\
            "set %s personality \"%s\"\n" % (distro, personality)]
            # Needs UDP and icmp support
        for item in ports:
            honeypot_config.append("add %s tcp port %s %s" % (distro, item, tcp))

        honeypot_config.append("set %s ethernet \"%s\"" % (distro, mac))
        honeypot_config.append("bind %s %s" % (ip, distro))

        print "Saved to honeypots/%s" % filename
        self.write_file("honeypots/%s" % filename, honeypot_config)

    def write_file(self, file, list):
        with open(file, "w+") as tmp:
            tmp.write("\n".join(list))

if __name__ == "__main__":
    dock = docker_build()
    dock.generate_dockerfile("honeyd.conf", ["1234"])
    dock.generate_honeypot(["1234", "4567"])
