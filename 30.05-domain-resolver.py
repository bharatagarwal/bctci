"""
# Domain Resolver

You manage a shared web hosting server with multiple IP addresses, and where multiple domains can share the same IP address. Each domain can have multiple subdomains.

Multiple IP addresses.
Multiple domains can share the same IP address.

Each domain can have multiple subdomains: does the subdomain resolve to the same IP address?

In DNS, it typically doesn't.

Implement a class, DomainResolver, that supports three methods:
- register_domain(ip, domain): associates a domain with an IP. You can assume that this function will be called at most once for a given domain.

- register_subdomain(domain, subdomain): adds a subdomain to a domain. You can assume that the domain will have been previously registered. Different domains can have a subdomain with the same name.

- has_subdomain(ip, domain, subdomain): returns whether there is a domain registered at that IP that has the given subdomain.

IPs, domains, and subdomains are strings.

Example 1:
resolver = DomainResolver()
resolver.register_domain("192.168.1.1", "example.com")
resolver.register_domain("192.168.1.1", "example.org")
resolver.register_domain("192.168.1.2", "domain.com")
resolver.register_subdomain("example.com", "a")
resolver.register_subdomain("example.com", "b")
resolver.has_subdomain("192.168.1.1", "example.com", "a")  # Returns True
resolver.has_subdomain("192.168.1.1", "example.com", "c")  # Returns False
resolver.has_subdomain("127.0.0.1", "example.com", "a")    # Returns False
resolver.has_subdomain("192.168.1.1", "example.org", "a")  # Returns False


domain has an ip address
domain has a list of subdomains
subdomain-domain can be present or not
ip has a list of domains

first check if ip has the domain
ip-domain set

domain-subdomain set
then check whether domain has sub-domain



Example 2:
resolver = DomainResolver()
resolver.register_domain("1.1.1.1", "test.com")
resolver.register_subdomain("test.com", "www")
resolver.has_subdomain("1.1.1.1", "test.com", "www")  # Returns True

Example 3:
resolver = DomainResolver()
resolver.has_subdomain("1.1.1.1", "test.com", "www")  # Returns False

Constraints:
- The number of calls to register_domain and register_subdomain will be at most 10^5
- The number of calls to has_subdomain will be at most 10^5
- All IPs follow the IPv4 format
- Each octet is a number between 0 and 255
- All domains and subdomains are non-empty strings of length at most 100
"""


class DomainResolver:
	def __init__(self):
		self.ip_domain_pairs = set()
		self.full_addresses = set()

	def register_domain(self, ip, domain):
		self.ip_domain_pairs.add(f"{ip}-{domain}")

	def register_subdomain(self, domain, subdomain):
		self.full_addresses.add(f"{subdomain}.{domain}")

	def has_subdomain(self, ip, domain, subdomain):
		answer = (
			f"{ip}-{domain}" in self.ip_domain_pairs
			and f"{subdomain}.{domain}" in self.full_addresses
		)
		print(answer)
		return answer


resolver = DomainResolver()
resolver.register_domain("192.168.1.1", "example.com")
resolver.register_domain("192.168.1.1", "example.org")
resolver.register_domain("192.168.1.2", "domain.com")
resolver.register_subdomain("example.com", "a")
resolver.register_subdomain("example.com", "b")
resolver.has_subdomain(
	"192.168.1.1", "example.com", "a"
)  # Returns True
resolver.has_subdomain(
	"192.168.1.1", "example.com", "c"
)  # Returns False
resolver.has_subdomain("127.0.0.1", "example.com", "a")  # Returns False
resolver.has_subdomain(
	"192.168.1.1", "example.org", "a"
)  # Returns False

print()

resolver = DomainResolver()
resolver.register_domain("1.1.1.1", "test.com")
resolver.register_subdomain("test.com", "www")
resolver.has_subdomain("1.1.1.1", "test.com", "www")  # Returns True

print()

resolver = DomainResolver()
resolver.has_subdomain("1.1.1.1", "test.com", "www")  # Returns False
