# SEEM3650 Practical Exam 2 Report

Name: LI BOHAN  
Student ID: 1155191403
Last three digits XYZ: 403  

## Shakespeare Character-level Model

### Generated Shakespeare Samples: First 5 Lines

KING RICHARD II:
Shall I be that set up your hands to my comfort?
DUKE OF YORK:
Then be petition enjoy'd my tents,
And I must be so too with me:


## Model Architecture Exploration

Since XYZ = 403, XYZ mod 4 = 3.

According to the assignment instruction, I fix the number of attention heads as 4 and vary the number of layers among 2, 3, 5, and 7.

| Number of Layers | Number of Heads | Loss at Chosen Iteration | Best Validation Loss |
|---|---:|---:|---:|
| 2 | 4 | 1.9509 | 1.9509 |
| 3 | 4 | 1.8577 | 1.8577 |
| 5 | 4 | 1.7200 | 1.7200 |
| 7 | 4 | 1.6461 | 1.6461 |

I used iteration 2000 as the consistent comparison point for all four architecture experiments because of the limited training time on Google Colab.

### Best Result

The lowest validation loss I achieved was 1.6461, produced by the setting with 7 layers and 4 attention heads on my machine.

The comparison plot is saved in `figures/loss_vs_layers_heads_4.png`.

## Training BabyGPT for Python Code Generation

Since XYZ = 403, XYZ mod 2 = 1.

Therefore, I use open-source Python code from GitHub as the dataset.

### Number of Tokens

377332

### Generated Code Samples: First 20 Lines

return base oplation)
def test_cookie_dict_ookies(self):
    os.cookies["foo"] = "the cookie"
      self._cookie = cokie.domain(cokies)
       self.cookies["ookie"] = "baze"
       self.cookies["foo"]
         r = self.cookie"
     def _cookie_dict_encoding(self):
        cookies = cookie.value, value
          jar.cookie_from_dict(key, domain=domain=0.cookies), cookies)
             assert cookies == cookielib.cookie()
    def test_cookie_cookie_dict(self, httpbin):
      prepare
def test_Proxy_envalues(self, httpbin):
       class:`HTTPServer("proxy", "Proxy_ies componsied").
       proxy_argentrip(
          "Unicodes be string in The suple."
         ""
       requests.adapters == proxy)
        except OSError(request, proxyError, esponse=rrequest)

### Favorite Generated Snippet

def test_cookie_dict_ookies(self):
    os.cookies["foo"] = "the cookie"
      self._cookie = cokie.domain(cokies)
       self.cookies["ookie"] = "baze"
       self.cookies["foo"]
         r = self.cookie"
     def _cookie_dict_encoding(self):
        cookies = cookie.value, value
          jar.cookie_from_dict(key, domain=domain=0.cookies), cookies)
             assert cookies == cookielib.cookie()
    def test_cookie_cookie_dict(self, httpbin):
      prepare
