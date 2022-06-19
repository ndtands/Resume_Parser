from auto_label.utils import *
from tqdm import tqdm
import warnings
import argparse
warnings.filterwarnings("ignore")

def main(path_in: str, path_out: str, path_datasource: str) -> None:
    auto_data = []
    # read init json
    data = read_json(path_in)

    # Auto label with pytesseract
    for dt in tqdm(data, desc='runs'):
        file = dt['file_upload']
        path = f'{path_datasource}/{file}'
        id_ = file.split('-')[0]
        extracted_pdf, (width, height) = extract_pdf(path)
        results = []
        for idx, line in enumerate(extracted_pdf):
            x, y, w, h, t = line
            result = fill_result(
                width=width,
                height=height,
                x=x,
                y=y,
                w=w,
                h=h,
                text=t,
                id=f'_{id_}{idx}'
            )
            results.extend(result)
        dt['annotations'][0]['result']= results
        auto_data.append(dt)
    
    # save auto label 
    write_json(auto_data, path= path_out)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Auto label for OCR")
    parser.add_argument('--path_in', type=str, default=str('init.json'), help="path of input", required=False)
    parser.add_argument('--path_out', type=str, default=str('auto_label.json'), help="path of output", required=False)
    parser.add_argument('--path_datasource', type=str, default=str('/mydata/media/upload/3'), help="path of database local for image", required=False)

    # Parse the argument
    args = parser.parse_args()
    path_in = args.path_in
    path_out = args.path_out
    path_datasource = args.path_datasource
    main(
        path_in=path_in, 
        path_out=path_out, 
        path_datasource=path_datasource
        )