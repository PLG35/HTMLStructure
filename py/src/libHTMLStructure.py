# -*-coding:Latin-1 -*
import urllib.request
import html.parser

class TestContent(html.parser.HTMLParser):
    def __init__(self, *args, **kwargs):
        super(TestContent, self).__init__(*args, **kwargs)

        # Default values of the test
        self.expectations = []
        self.tag = ""
        self.attribute = ""

        # Results
        self.found = []
        self.failures = []
        self.success = []

    def setCriteria(self, tag, attribute, expectations):
        # Set values of the test
        self.expectations = expectations
        self.tag = tag
        self.attribute = attribute

    def handle_starttag(self, tag, attrs):
        if(tag == self.tag):
            for i in range(len(attrs)):
                if attrs[i][0] == self.attribute and attrs[i][1].encode('latin-1', 'backslashreplace').decode('unicode-escape') in self.expectations:
                    self.found.append(attrs[i][1].encode('latin-1', 'backslashreplace').decode('unicode-escape'))

    def getResult(self):
        for expectation in self.expectations:
            if expectation not in self.found:
                self.failures.append([self.tag, self.attribute, expectation])
            else:
                self.success.append([self.tag, self.attribute, expectation])

class TestURL:

    def __init__(self, url, testDefinition):
        # Variables of the test
        self.myURL = url
        self.openFailed = False

        # Test the validity of the url
        try:
            self.urlOpened = urllib.request.urlopen(self.myURL) # In python 2.7, urllib.request should be replaced by urllib
            htmlContent = self.urlOpened.read()
        except urllib.error.HTTPError as HTTPError:
            self.openFailed = {'status':'failed', 'errorType':'HTTPError', 'errorCode':HTTPError.code, 'errorReason':HTTPError.reason, 'errorHeaders':HTTPError.headers}
        except urllib.error.URLError as URLError:
            self.openFailed = {'status':'failed', 'errorType':'URLError', 'errorReason':URLError.reason}

        # Parse content of the html if url is valid
        if not self.openFailed:
            # Get html data
            self.strHtml = str(htmlContent)

            # Launch test on data
            myParser = TestContent()
            myParser.setCriteria(testDefinition[0], testDefinition[1], testDefinition[2])
            myParser.feed(self.strHtml)
            myParser.getResult()

        # Display results
        self.output = ""
        if self.openFailed:
            self.output = str(self.openFailed)
        else:
            if len(myParser.failures) > 0:
                self.output = str({'status':'failed', 'errorType':'StructureError', 'results': {'found': myParser.success, 'missing':myParser.failures}})
            else:
                self.output = str({'status':'passed', 'results': {'found': myParser.success, 'missing':myParser.failures}})
