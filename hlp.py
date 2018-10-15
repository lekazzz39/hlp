import click
from dns.resolver import query as dns_query
import whois

@click.command()
@click.argument('domain')
def main(domain):
	ids = [
		'A',
		'NS',
		'CNAME',
		'PTR',
		'MX',
		'TXT',
		'AAAA',
		'SPF',
		]
	whois_response = whois.whois(domain)
	print(whois_response.text)
	for a in ids:
		print('----------------------------------------------------------------------')
		try:
			answer = dns_query(domain, a)
			for rdata in answer:
				print(a, ':', rdata.to_text())

		except Exception as e:
				pass

if __name__ == "__main__":
    main()