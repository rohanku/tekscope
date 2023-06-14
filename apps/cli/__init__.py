import argparse
import matplotlib.pyplot as plt

from tekscope import Oscilloscope
from tekscope.transfer import retrieve_all_waveforms, retrieve_waveform
from tekscope.io import save_waveform, save_waveforms, load_waveforms


def transfer(args):
    osc = Oscilloscope(host=args.host, port=args.port)
    output = args.output if args.output else "data.tek"

    with open(output, "wb") as f:
        if args.all:
            wfs = osc.retrieve_all_waveforms()
            save_waveforms(f, wfs)
        elif args.source:
            wf = osc.retrieve_waveform(args.source)
            save_waveform(f, wf)


def display(args):
    wfs = load_waveforms(args.tekfile)
    plt.figure()
    for wf in wfs.all():
        plt.plot(wf.t(), wf.v(), label=wf.channel)
    plt.legend()
    plt.show()


parser = argparse.ArgumentParser(
    prog="tekscope", description="CLI for interacting with a Tektronix oscilloscope"
)
parser.add_argument("-H", "--host", default="169.254.8.194")
parser.add_argument("-P", "--port", type=int, default=4000)

subparsers = parser.add_subparsers(required=True)

parser_transfer = subparsers.add_parser(
    "transfer", help="Transfer waveforms between devices."
)
group = parser_transfer.add_mutually_exclusive_group(required=True)
group.add_argument("-s", "--source")
group.add_argument("-a", "--all", action="store_true")
parser_transfer.add_argument("-o", "--output")
parser_transfer.set_defaults(func=transfer)

parser_display = subparsers.add_parser("display", help="Display waveforms.")
parser_display.add_argument("tekfile")
parser_display.set_defaults(func=display)


def main():
    args = parser.parse_args()
    args.func(args)
