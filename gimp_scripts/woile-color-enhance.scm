; === Batch Auto color enhance ===
;
; This program is distributed in the hope that it will be useful,
; but WITHOUT ANY WARRANTY; without even the implied warranty of
; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
; GNU General Public License for more details.
;
; Feel free to re-use and distribute at will.
;
; Files are saved with the extension _ce
;
; Author: github.com/woile

(define (woile-color-enhance pattern)
  ; file list
  (let* ((filelist (cadr (file-glob pattern 1))))
    ; loop all
    (while (not (null? filelist))
           ; load
           (let* ((filename (car filelist))
                  (customfilename (unbreakupstr (butlast (strbreakup filename ".")) "."))
                  (nfilename (string-append customfilename "_ce.jpg"))
                  (image (car (gimp-file-load RUN-NONINTERACTIVE filename filename)))
                  (drawable (car (gimp-image-get-active-layer image))))
             ; process
             (plug-in-color-enhance RUN-NONINTERACTIVE image drawable)
             ; save
             (gimp-file-save RUN-NONINTERACTIVE image drawable nfilename nfilename)
             (gimp-image-delete image))
           ; next
           (set! filelist (cdr filelist)))))